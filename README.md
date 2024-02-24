Commands in terminal after cloning:--new one--
	1. "  cd to sql_data directory   "
	2. "  docker build -t "dbs" .   "
	3. "  cd ..   "
	4. "  docker run -it --name mysql-fastapi -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3456:3306 -d dbs
	5. "  flask --app login_index.py run / python3 login_index.py  "
