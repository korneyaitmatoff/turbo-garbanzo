create table cars (
    id UUID primary key,
    name varchar,
    cost money,
    is_writeoff boolean default false,
    is_rented boolean default false
);