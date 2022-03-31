# Web

# Flag: picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}

Connect to this PostgreSQL server and find the flag! psql -h saturn.picoctf.net -p 56673 -U postgres pico Password is postgres

pico=# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres

 pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)