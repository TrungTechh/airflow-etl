FROM mysql:8.0.35-debian

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=bike_store
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root

# Copy SQL scripts to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/init.sql

RUN chmod +x /docker-entrypoint-initdb.d/init.sql

# Expose the MySQL port
EXPOSE 3306