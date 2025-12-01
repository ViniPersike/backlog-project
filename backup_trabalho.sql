--
-- PostgreSQL database dump
--

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

-- Started on 2025-12-01 00:01:37

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 222 (class 1259 OID 17289)
-- Name: developers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.developers (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.developers OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17288)
-- Name: developers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.developers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.developers_id_seq OWNER TO postgres;

--
-- TOC entry 5064 (class 0 OID 0)
-- Dependencies: 221
-- Name: developers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.developers_id_seq OWNED BY public.developers.id;


--
-- TOC entry 227 (class 1259 OID 17330)
-- Name: game_genres; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_genres (
    game_id integer NOT NULL,
    genre_id integer NOT NULL
);


ALTER TABLE public.game_genres OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17300)
-- Name: games; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.games (
    id integer NOT NULL,
    name text NOT NULL,
    release_year integer,
    developer_id integer NOT NULL
);


ALTER TABLE public.games OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 17299)
-- Name: games_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.games_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.games_id_seq OWNER TO postgres;

--
-- TOC entry 5065 (class 0 OID 0)
-- Dependencies: 223
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.games_id_seq OWNED BY public.games.id;


--
-- TOC entry 220 (class 1259 OID 17278)
-- Name: genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.genre OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 17277)
-- Name: genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.genre_id_seq OWNER TO postgres;

--
-- TOC entry 5066 (class 0 OID 0)
-- Dependencies: 219
-- Name: genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genre_id_seq OWNED BY public.genre.id;


--
-- TOC entry 228 (class 1259 OID 17347)
-- Name: user_games; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_games (
    user_id integer NOT NULL,
    game_id integer NOT NULL,
    rating real,
    "time" integer,
    status text,
    review text
);


ALTER TABLE public.user_games OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 17317)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name text NOT NULL,
    password text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 17316)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 5067 (class 0 OID 0)
-- Dependencies: 225
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 4880 (class 2604 OID 17292)
-- Name: developers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.developers ALTER COLUMN id SET DEFAULT nextval('public.developers_id_seq'::regclass);


--
-- TOC entry 4881 (class 2604 OID 17303)
-- Name: games id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games ALTER COLUMN id SET DEFAULT nextval('public.games_id_seq'::regclass);


--
-- TOC entry 4879 (class 2604 OID 17281)
-- Name: genre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre ALTER COLUMN id SET DEFAULT nextval('public.genre_id_seq'::regclass);


--
-- TOC entry 4882 (class 2604 OID 17320)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 5052 (class 0 OID 17289)
-- Dependencies: 222
-- Data for Name: developers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.developers VALUES (1, 'Fromsoftware');
INSERT INTO public.developers VALUES (2, 'Team Cherry');
INSERT INTO public.developers VALUES (3, 'Rockstar');
INSERT INTO public.developers VALUES (4, 'Santa Monica Studio');
INSERT INTO public.developers VALUES (5, 'Valve');
INSERT INTO public.developers VALUES (6, 'Bethesda');
INSERT INTO public.developers VALUES (7, 'Obsidian');
INSERT INTO public.developers VALUES (8, 'Insomniac');
INSERT INTO public.developers VALUES (9, 'Square Enix');
INSERT INTO public.developers VALUES (10, 'Konami');
INSERT INTO public.developers VALUES (11, 'Sega');


--
-- TOC entry 5057 (class 0 OID 17330)
-- Dependencies: 227
-- Data for Name: game_genres; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.game_genres VALUES (1, 1);
INSERT INTO public.game_genres VALUES (1, 3);
INSERT INTO public.game_genres VALUES (1, 4);
INSERT INTO public.game_genres VALUES (1, 5);
INSERT INTO public.game_genres VALUES (1, 8);
INSERT INTO public.game_genres VALUES (2, 2);
INSERT INTO public.game_genres VALUES (2, 5);
INSERT INTO public.game_genres VALUES (3, 3);
INSERT INTO public.game_genres VALUES (3, 5);
INSERT INTO public.game_genres VALUES (3, 8);
INSERT INTO public.game_genres VALUES (4, 1);
INSERT INTO public.game_genres VALUES (4, 3);
INSERT INTO public.game_genres VALUES (4, 5);
INSERT INTO public.game_genres VALUES (4, 8);
INSERT INTO public.game_genres VALUES (5, 1);
INSERT INTO public.game_genres VALUES (5, 4);
INSERT INTO public.game_genres VALUES (5, 5);
INSERT INTO public.game_genres VALUES (5, 8);
INSERT INTO public.game_genres VALUES (5, 9);
INSERT INTO public.game_genres VALUES (6, 1);
INSERT INTO public.game_genres VALUES (6, 4);
INSERT INTO public.game_genres VALUES (6, 5);
INSERT INTO public.game_genres VALUES (6, 8);
INSERT INTO public.game_genres VALUES (6, 9);
INSERT INTO public.game_genres VALUES (7, 3);
INSERT INTO public.game_genres VALUES (7, 4);
INSERT INTO public.game_genres VALUES (7, 5);
INSERT INTO public.game_genres VALUES (7, 8);
INSERT INTO public.game_genres VALUES (8, 8);
INSERT INTO public.game_genres VALUES (8, 7);
INSERT INTO public.game_genres VALUES (9, 10);
INSERT INTO public.game_genres VALUES (10, 4);
INSERT INTO public.game_genres VALUES (10, 5);
INSERT INTO public.game_genres VALUES (10, 8);
INSERT INTO public.game_genres VALUES (11, 4);
INSERT INTO public.game_genres VALUES (11, 5);
INSERT INTO public.game_genres VALUES (11, 8);
INSERT INTO public.game_genres VALUES (12, 8);
INSERT INTO public.game_genres VALUES (12, 7);


--
-- TOC entry 5054 (class 0 OID 17300)
-- Dependencies: 224
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.games VALUES (1, 'Elden Ring', 2023, 1);
INSERT INTO public.games VALUES (2, 'Counter-Strike', 2012, 5);
INSERT INTO public.games VALUES (3, 'Final Fantasy XVI', 2024, 9);
INSERT INTO public.games VALUES (4, 'Dark Souls III', 2016, 1);
INSERT INTO public.games VALUES (5, 'Hollow Knight', 2017, 2);
INSERT INTO public.games VALUES (6, 'Hollow Knight Silksong', 2025, 2);
INSERT INTO public.games VALUES (7, 'The Elder Scrolls V Skyrim', 2011, 6);
INSERT INTO public.games VALUES (8, 'Sonic The Hedgehog', 1991, 11);
INSERT INTO public.games VALUES (9, 'PES 2018', 2017, 10);
INSERT INTO public.games VALUES (10, 'Red Dead Redemption', 2010, 3);
INSERT INTO public.games VALUES (11, 'Grand Theft Auto V', 2013, 3);
INSERT INTO public.games VALUES (12, 'Ratchet & Clank', 2016, 8);


--
-- TOC entry 5050 (class 0 OID 17278)
-- Dependencies: 220
-- Data for Name: genre; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genre VALUES (1, 'Soulslike');
INSERT INTO public.genre VALUES (2, 'FPS');
INSERT INTO public.genre VALUES (3, 'RPG');
INSERT INTO public.genre VALUES (4, 'Mundo Aberto');
INSERT INTO public.genre VALUES (5, 'Ação');
INSERT INTO public.genre VALUES (7, 'Plataforma');
INSERT INTO public.genre VALUES (8, 'Aventura');
INSERT INTO public.genre VALUES (9, 'Metroidvania');
INSERT INTO public.genre VALUES (10, 'Esportes');


--
-- TOC entry 5058 (class 0 OID 17347)
-- Dependencies: 228
-- Data for Name: user_games; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.user_games VALUES (2, 5, 10, 75, 'Finalizado', 'Excelente!');
INSERT INTO public.user_games VALUES (2, 1, 10, 120, 'Finalizado', 'Dificil, mas incrível');
INSERT INTO public.user_games VALUES (2, 4, 0, 0, 'Quero Jogar', '');
INSERT INTO public.user_games VALUES (2, 6, 9.5, 20, 'Jogando', '');
INSERT INTO public.user_games VALUES (4, 1, 10, 100, 'Finalizado', 'Ótimo jogo, gostei muito');
INSERT INTO public.user_games VALUES (4, 11, 8, 35, 'Finalizado', 'Legal');
INSERT INTO public.user_games VALUES (4, 3, 5, 15, 'Abandonado', 'Não gostei da história');
INSERT INTO public.user_games VALUES (4, 9, 8, 75, 'Jogando', 'Legal pra jogar com os amigos');
INSERT INTO public.user_games VALUES (7, 12, 9.2, 38, 'Finalizado', '');
INSERT INTO public.user_games VALUES (7, 7, 10, 300, 'Jogando', 'Melhor jogo já criado');
INSERT INTO public.user_games VALUES (7, 4, 7, 60, 'Finalizado', 'Muito dificil');
INSERT INTO public.user_games VALUES (7, 8, 8, 15, 'Finalizado', 'Legal, nostálgico');
INSERT INTO public.user_games VALUES (6, 1, 4, 30, 'Abandonado', 'Péssimo, combate muito dificil');
INSERT INTO public.user_games VALUES (6, 2, 9, 1200, 'Jogando', '');
INSERT INTO public.user_games VALUES (6, 9, 10, 149, 'Jogando', 'Melhor jogo da história');
INSERT INTO public.user_games VALUES (3, 2, 8, 2000, 'Jogando', 'Prefiro Rainbow Six');
INSERT INTO public.user_games VALUES (7, 3, 10, 80, 'Finalizado', 'História incrível');


--
-- TOC entry 5056 (class 0 OID 17317)
-- Dependencies: 226
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users VALUES (1, 'admin', '123');
INSERT INTO public.users VALUES (2, 'vini', '123123');
INSERT INTO public.users VALUES (3, 'lucas', '321');
INSERT INTO public.users VALUES (4, 'zapi', '456');
INSERT INTO public.users VALUES (5, 'rafael', '789');
INSERT INTO public.users VALUES (6, 'gabriel', '765');
INSERT INTO public.users VALUES (7, 'julio', '999');


--
-- TOC entry 5068 (class 0 OID 0)
-- Dependencies: 221
-- Name: developers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.developers_id_seq', 11, true);


--
-- TOC entry 5069 (class 0 OID 0)
-- Dependencies: 223
-- Name: games_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.games_id_seq', 12, true);


--
-- TOC entry 5070 (class 0 OID 0)
-- Dependencies: 219
-- Name: genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genre_id_seq', 10, true);


--
-- TOC entry 5071 (class 0 OID 0)
-- Dependencies: 225
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 7, true);


--
-- TOC entry 4886 (class 2606 OID 17298)
-- Name: developers developers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.developers
    ADD CONSTRAINT developers_pkey PRIMARY KEY (id);


--
-- TOC entry 4894 (class 2606 OID 17336)
-- Name: game_genres game_genres_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_genres
    ADD CONSTRAINT game_genres_pkey PRIMARY KEY (game_id, genre_id);


--
-- TOC entry 4888 (class 2606 OID 17310)
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (id);


--
-- TOC entry 4884 (class 2606 OID 17287)
-- Name: genre genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (id);


--
-- TOC entry 4896 (class 2606 OID 17355)
-- Name: user_games user_games_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_games
    ADD CONSTRAINT user_games_pkey PRIMARY KEY (user_id, game_id);


--
-- TOC entry 4890 (class 2606 OID 17329)
-- Name: users users_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_name_key UNIQUE (name);


--
-- TOC entry 4892 (class 2606 OID 17327)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 4898 (class 2606 OID 17337)
-- Name: game_genres game_genres_game_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_genres
    ADD CONSTRAINT game_genres_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.games(id) ON DELETE CASCADE;


--
-- TOC entry 4899 (class 2606 OID 17342)
-- Name: game_genres game_genres_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_genres
    ADD CONSTRAINT game_genres_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public.genre(id) ON DELETE CASCADE;


--
-- TOC entry 4897 (class 2606 OID 17311)
-- Name: games games_developer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_developer_id_fkey FOREIGN KEY (developer_id) REFERENCES public.developers(id) ON DELETE CASCADE;


--
-- TOC entry 4900 (class 2606 OID 17361)
-- Name: user_games user_games_game_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_games
    ADD CONSTRAINT user_games_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.games(id) ON DELETE CASCADE;


--
-- TOC entry 4901 (class 2606 OID 17356)
-- Name: user_games user_games_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_games
    ADD CONSTRAINT user_games_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


-- Completed on 2025-12-01 00:01:37

--
-- PostgreSQL database dump complete
--
