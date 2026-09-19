
mkdir templates 
python3 scaffold.py city name country_id:references
python3 scaffold.py user username password email phone country_id:references pic:file
python3 scaffold.py country name
python3 scaffold.py morceau_a_jouer name
python3 scaffold.py simplescore title_score composer myscore:staff pic time_signature key_signature city_id:references edition user_id:references morceau_a_jouer_id:references
python3 scaffold.py simplerecording video:radio vid:file simplescore_id:references
