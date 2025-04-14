CREATE TABLE public.cars (
	id uuid DEFAULT gen_random_uuid() NOT NULL,
	"name" varchar NULL,
	"cost" money NULL,
	is_writeoff bool DEFAULT false NULL,
	is_rented bool DEFAULT false NULL,
	CONSTRAINT cars_pkey PRIMARY KEY (id)
);