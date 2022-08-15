--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin; Type: TABLE; Schema: public; Owner: excalibur
--

CREATE TABLE public.admin (
    id integer NOT NULL,
    username character varying(60),
    title character varying(60),
    clearance character varying(40),
    password_hash character varying(200)
);


ALTER TABLE public.admin OWNER TO excalibur;

--
-- Name: admin_id_seq; Type: SEQUENCE; Schema: public; Owner: excalibur
--

CREATE SEQUENCE public.admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_id_seq OWNER TO excalibur;

--
-- Name: admin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: excalibur
--

ALTER SEQUENCE public.admin_id_seq OWNED BY public.admin.id;


--
-- Name: player; Type: TABLE; Schema: public; Owner: excalibur
--

CREATE TABLE public.player (
    id integer NOT NULL,
    first_name character varying(40),
    last_name character varying(40),
    school character varying(80),
    sport character varying(40),
    "position" character varying(50),
    img1_url character varying(500),
    img2_url character varying(500)
);


ALTER TABLE public.player OWNER TO excalibur;

--
-- Name: player_id_seq; Type: SEQUENCE; Schema: public; Owner: excalibur
--

CREATE SEQUENCE public.player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_id_seq OWNER TO excalibur;

--
-- Name: player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: excalibur
--

ALTER SEQUENCE public.player_id_seq OWNED BY public.player.id;


--
-- Name: shop_item; Type: TABLE; Schema: public; Owner: excalibur
--

CREATE TABLE public.shop_item (
    id integer NOT NULL,
    name character varying(140),
    price integer,
    img1_url character varying(1000),
    img2_url character varying(1000),
    player_id integer
);


ALTER TABLE public.shop_item OWNER TO excalibur;

--
-- Name: shop_item_id_seq; Type: SEQUENCE; Schema: public; Owner: excalibur
--

CREATE SEQUENCE public.shop_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shop_item_id_seq OWNER TO excalibur;

--
-- Name: shop_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: excalibur
--

ALTER SEQUENCE public.shop_item_id_seq OWNED BY public.shop_item.id;


--
-- Name: admin id; Type: DEFAULT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.admin ALTER COLUMN id SET DEFAULT nextval('public.admin_id_seq'::regclass);


--
-- Name: player id; Type: DEFAULT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.player ALTER COLUMN id SET DEFAULT nextval('public.player_id_seq'::regclass);


--
-- Name: shop_item id; Type: DEFAULT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.shop_item ALTER COLUMN id SET DEFAULT nextval('public.shop_item_id_seq'::regclass);


--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: excalibur
--

COPY public.admin (id, username, title, clearance, password_hash) FROM stdin;
1	Sean Fagan	Sultan of Codes	Midnight	pbkdf2:sha256:260000$Ipo2EUPZ$8659f48f416602282e7592f6caa0fe232819c33b046cb0794c57b1ddb7abcee3
\.


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: excalibur
--

COPY public.player (id, first_name, last_name, school, sport, "position", img1_url, img2_url) FROM stdin;
1	Bella	Wright	Snowniversity	Cross Country Ski	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/10/bella-wrigth-cover.jpg	https://oncoormarketing.com/wp-content/uploads/2021/10/wright.jpg
2	Britain	Covey	University of Utah	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/10/client-6.jpg	https://oncoormarketing.com/wp-content/uploads/2021/10/BritainCovey.png
3	Sean	Clifford	Penn State Nittany	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/10/client-1.jpg?w=980&ssl=1	https://oncoormarketing.com/wp-content/uploads/2021/10/sean.jpg
4	Calvin	Knapp	Germantown University	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/calvin-knapp-cover2.jpg	https://oncoormarketing.com/wp-content/uploads/2021/11/calvin-knapp-banner.jpg
5	Kingsley	Suamataia	Brigham Young University	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/12/Kingsley-Suamataia-cover.jpg	https://oncoormarketing.com/wp-content/uploads/2021/12/Kingsley-Suamataia-banner.jpg
6	Brock	Miller	Brigham Young University	Basketball	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/brock-miller-cover.jpg	https://oncoormarketing.com/wp-content/uploads/2021/11/brock-miller-banner.jpg
7	Chaz	Ah	Brigham Young University	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/10/chaz-cover5.png	1https://oncoormarketing.com/wp-content/uploads/2021/10/chazahyou-banner.png
8	Derek	Wright	Utah State University	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/derek-wright-cover.jpg	https://oncoormarketing.com/wp-content/uploads/2021/11/derek-wright-banner.jpg
9	Logan	Bonner	Utah State University	Football	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Caleb-Bonner-cover.jpg	https://oncoormarketing.com/wp-content/uploads/2021/11/logan-bonner-banner.jpg
10	Justin	Bean	University	Basketball	\N	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/JustineBean.png	https://oncoormarketing.com/wp-content/uploads/2021/10/justinebean-banner.png
\.


--
-- Data for Name: shop_item; Type: TABLE DATA; Schema: public; Owner: excalibur
--

COPY public.shop_item (id, name, price, img1_url, img2_url, player_id) FROM stdin;
1	Ski Pole	5000	https://www.voile.com/mm5/graphics/00000001/camlock-2.jpg	https://cdn.shopify.com/s/files/1/0277/1345/products/PolesSquare_1920x.png	1
2	Covey UofU Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Britain-Cover-shirt-1st.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Britain-Cover-shirt-2nd.png	2
3	Sean Clifford Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Sean-Clifford-T-shirt-2.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Sean-Clifford-Logo-2.png	3
4	Germantown Roots Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Calvin-Knapp-2nd-Shirt.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Calin-Knapp-2nd-shirt-logo.png	4
5	King Kingsley Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/12/Kingsley-Suamataia-Shirt.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/12/Kingsley-Suamataia-Logo.png	5
6	Be Smooth Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Brock-Miller-Shirt.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/T-shirt-logo.png	6
7	Chaz Ah You Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Screen-Shot-2021-11-17-at-5.28.23-PM.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Screen-Shot-2021-11-17-at-5.28.42-PM.png	7
8	Wright Place Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Derek-Wright-1st-Shirt.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Derek-Wright-1st-Logo.png	1
9	Cowboy Bonner Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Caleb-Bonner-Shirt.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Caleb-Bonner-Logo.png	9
10	JB34 Shirt	29	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Justin-Bean-T-shirt-2.png	https://i0.wp.com/oncoormarketing.com/wp-content/uploads/2021/11/Justin-Bean-Logo-2.png	10
\.


--
-- Name: admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: excalibur
--

SELECT pg_catalog.setval('public.admin_id_seq', 1, true);


--
-- Name: player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: excalibur
--

SELECT pg_catalog.setval('public.player_id_seq', 10, true);


--
-- Name: shop_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: excalibur
--

SELECT pg_catalog.setval('public.shop_item_id_seq', 10, true);


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);


--
-- Name: player player_pkey; Type: CONSTRAINT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (id);


--
-- Name: shop_item shop_item_pkey; Type: CONSTRAINT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.shop_item
    ADD CONSTRAINT shop_item_pkey PRIMARY KEY (id);


--
-- Name: shop_item shop_item_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: excalibur
--

ALTER TABLE ONLY public.shop_item
    ADD CONSTRAINT shop_item_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.player(id);


--
-- PostgreSQL database dump complete
--

