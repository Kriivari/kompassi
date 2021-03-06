BEGIN;
REVOKE ALL ON DATABASE kompassi FROM PUBLIC;
REVOKE ALL ON DATABASE kompassi FROM kompassi;
GRANT CONNECT ON DATABASE kompassi TO kompassi;

REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM kompassi;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM PUBLIC;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM kompassi;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO kompassi;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO kompassi;

REVOKE ALL ON event_log_entry FROM kompassi;
GRANT SELECT, INSERT ON event_log_entry TO kompassi;

REVOKE ALL ON django_migrations FROM kompassi;
GRANT SELECT ON django_migrations TO kompassi;

REVOKE ALL ON django_admin_log FROM kompassi;
GRANT SELECT, INSERT on django_admin_log TO kompassi;
COMMIT;
