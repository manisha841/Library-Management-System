CREATE MIGRATION m17s2tswynm635anml2ci7ly2pa2nck2rcbvrhlznptqdoqa4t2pia
    ONTO initial
{
  CREATE TYPE default::Category {
      CREATE REQUIRED PROPERTY name: std::str {
          CREATE CONSTRAINT std::max_len_value(100);
      };
  };
  CREATE TYPE default::Book {
      CREATE REQUIRED LINK category: default::Category;
      CREATE PROPERTY author: std::str {
          CREATE CONSTRAINT std::max_len_value(200);
      };
      CREATE REQUIRED PROPERTY title: std::str {
          CREATE CONSTRAINT std::max_len_value(200);
      };
  };
  CREATE TYPE default::User {
      CREATE MULTI LINK borrowed_books: default::Book;
      CREATE PROPERTY full_name: std::str {
          CREATE CONSTRAINT std::max_len_value(200);
      };
      CREATE REQUIRED PROPERTY username: std::str {
          CREATE CONSTRAINT std::max_len_value(100);
      };
  };
};
