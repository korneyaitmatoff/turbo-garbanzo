CREATE TABLE public.cars (
	id uuid DEFAULT gen_random_uuid() NOT NULL,
	"name" varchar NULL,
	"cost" money NULL,
	is_writeoff bool DEFAULT false NULL,
	is_rented bool DEFAULT false NULL,
	CONSTRAINT cars_pkey PRIMARY KEY (id)
);

INSERT INTO public.cars (id, name, cost, is_writeoff, is_rented)
SELECT
    gen_random_uuid(),
    (ARRAY['Toyota', 'Honda', 'BMW', 'Mercedes', 'Ford', 'Kia', 'Hyundai', 'Lada', 'Volkswagen', 'Chevrolet'])[floor(random() * 10 + 1)],
    (random() * 40000 + 10000)::numeric::money,
    (random() < 0.5),
    (random() < 0.5)
FROM generate_series(1, 10);