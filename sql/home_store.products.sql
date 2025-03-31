CREATE TABLE public.products (
	item varchar NULL,
	price numeric NULL,
	CONSTRAINT products_unique UNIQUE (item,price)
);