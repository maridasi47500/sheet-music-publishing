CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists city(
        id integer primary key autoincrement,
        name text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            password text,
            email text,
            phone text,
            country_id text,
            pic text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists country(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists morceau_a_jouer(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists simplescore(
        id integer primary key autoincrement,
        title_score text,
            composer text,
            myscore text,
            pic text,
            time_signature text,
            key_signature text,
            city_id text,
            edition text,
            user_id text,
            morceau_a_jouer_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists simplerecording(
        id integer primary key autoincrement,
        video text,
            vid text,
            simplescore_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
insert or ignore into morceau_a_jouer (name) values ('capriccio');

insert or ignore  into morceau_a_jouer (name) values ('menuet');

insert or ignore  into morceau_a_jouer (name) values ('adagio');

insert or ignore  into morceau_a_jouer (name) values ('advanced exercices');

insert or ignore  into morceau_a_jouer (name) values ('studies');

insert or ignore  into morceau_a_jouer (name) values ('air');

insert or ignore  into morceau_a_jouer (name) values ('albumblatt');

insert or ignore  into morceau_a_jouer (name) values ('allegro');

insert or ignore  into morceau_a_jouer (name) values ('allemande');

insert or ignore  into morceau_a_jouer (name) values ('amuseent');

insert or ignore  into morceau_a_jouer (name) values ('amusement');

insert or ignore  into morceau_a_jouer (name) values ('aria');

insert or ignore  into morceau_a_jouer (name) values ('arioso');

insert or ignore  into morceau_a_jouer (name) values ('aubade');

insert or ignore  into morceau_a_jouer (name) values ('ballade');

insert or ignore  into morceau_a_jouer (name) values ('quartet');

insert or ignore  into morceau_a_jouer (name) values ('berceuse');

insert or ignore  into morceau_a_jouer (name) values ('cadenza');

insert or ignore  into morceau_a_jouer (name) values ('cantata');

insert or ignore  into morceau_a_jouer (name) values ('canzonetta');

insert or ignore  into morceau_a_jouer (name) values ('sonata');

insert or ignore  into morceau_a_jouer (name) values ('sonatina');

insert or ignore  into morceau_a_jouer (name) values ('chamber concerto*');

insert or ignore  into morceau_a_jouer (name) values ('ciaccona');

insert or ignore  into morceau_a_jouer (name) values ('chanson');

insert or ignore  into morceau_a_jouer (name) values ('chant');

insert or ignore  into morceau_a_jouer (name) values ('church sonata');

insert or ignore  into morceau_a_jouer (name) values ('trio');

insert or ignore  into morceau_a_jouer (name) values ('concert');

insert or ignore  into morceau_a_jouer (name) values ('concert etude');

insert or ignore  into morceau_a_jouer (name) values ('concert fantaisie');

insert or ignore  into morceau_a_jouer (name) values ('concerto');

insert or ignore  into morceau_a_jouer (name) values ('concertino');

insert or ignore  into morceau_a_jouer (name) values ('danses');

insert or ignore  into morceau_a_jouer (name) values ('diversions');

insert or ignore  into morceau_a_jouer (name) values ('divertissement');

insert or ignore  into morceau_a_jouer (name) values ('duet');

insert or ignore  into morceau_a_jouer (name) values ('duo brillant');

insert or ignore  into morceau_a_jouer (name) values ('etude');

insert or ignore  into morceau_a_jouer (name) values ('elegie');

insert or ignore  into morceau_a_jouer (name) values ('fantaisie');

insert or ignore  into morceau_a_jouer (name) values ('quintet');

insert or ignore  into morceau_a_jouer (name) values ('fugue');

insert or ignore  into morceau_a_jouer (name) values ('gavotte');

insert or ignore  into morceau_a_jouer (name) values ('intermezzo');

insert or ignore  into morceau_a_jouer (name) values ('brillante variation');

insert or ignore  into morceau_a_jouer (name) values ('passacaglia');

insert or ignore  into morceau_a_jouer (name) values ('polonaise');

insert or ignore  into morceau_a_jouer (name) values ('rondo');

insert or ignore  into morceau_a_jouer (name) values ('larghetto');

insert or ignore  into morceau_a_jouer (name) values ('largo');

insert or ignore  into morceau_a_jouer (name) values ('mazurka');

insert or ignore  into morceau_a_jouer (name) values ('meditation');

insert or ignore  into morceau_a_jouer (name) values ('melodie');

insert or ignore  into morceau_a_jouer (name) values ('morceaux');

insert or ignore  into morceau_a_jouer (name) values ('mouvement');

insert or ignore  into morceau_a_jouer (name) values ('nocturne');

insert or ignore  into morceau_a_jouer (name) values ('partitia');

insert or ignore  into morceau_a_jouer (name) values ('partita');

insert or ignore  into morceau_a_jouer (name) values ('ouverture-suite');

insert or ignore  into morceau_a_jouer (name) values ('poème');

insert or ignore  into morceau_a_jouer (name) values ('sextet');

insert or ignore  into morceau_a_jouer (name) values ('potpourri');

insert or ignore  into morceau_a_jouer (name) values ('préludce');

insert or ignore  into morceau_a_jouer (name) values ('prélude');

insert or ignore  into morceau_a_jouer (name) values ('presto');

insert or ignore  into morceau_a_jouer (name) values ('psalm');

insert or ignore  into morceau_a_jouer (name) values ('rêverie');

insert or ignore  into morceau_a_jouer (name) values ('romance');

insert or ignore  into morceau_a_jouer (name) values ('rondeau');

insert or ignore  into morceau_a_jouer (name) values ('sérénade');

insert or ignore  into morceau_a_jouer (name) values ('symphnie');

insert or ignore  into morceau_a_jouer (name) values ('symphonie');

insert or ignore  into morceau_a_jouer (name) values ('solo');

insert or ignore  into morceau_a_jouer (name) values ('suite');

insert or ignore  into morceau_a_jouer (name) values ('thème and variations');

insert or ignore  into morceau_a_jouer (name) values ('variations');

insert or ignore  into morceau_a_jouer (name) values ('zigeunerweisen');
