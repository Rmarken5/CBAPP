import connection_settings as conn


def main():
	connection = conn.createConnection();
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL database... MySQL Server version on ",db_Info)

if __name__ == '__main__':
	main()