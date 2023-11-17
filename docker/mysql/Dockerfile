FROM mysql:8.0.35-debian

# Copy SQL scripts to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/init.sql

RUN chmod +x /docker-entrypoint-initdb.d/init.sql

# Expose the MySQL port
EXPOSE 3306

ENTRYPOINT [ "./entrypoint.sh" ]