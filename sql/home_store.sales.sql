CREATE TABLE public.sales (
	dt date NULL,
	doc_id varchar NULL,
	item varchar NULL,
	category varchar NULL,
	amount int NULL,
	price numeric NULL,
	discount numeric NULL,
	CONSTRAINT sales_unique UNIQUE (dt,doc_id,item,category,amount,price,discount)
);

