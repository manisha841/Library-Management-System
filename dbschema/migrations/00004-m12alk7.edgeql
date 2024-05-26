CREATE MIGRATION m12alk7vjcpalmqgbtcqx7twdnds552axlqn2cnhxdbjw6mvdsbimq
    ONTO m1enqsdd2cahy46rb7xcrb7yrdln5wsguhxbwflatsnf3ewudw2z4q
{
  ALTER TYPE default::User {
      DROP PROPERTY username;
  };
};
