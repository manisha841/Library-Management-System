CREATE MIGRATION m1hxkeqhtf57a5lriexnrlum77uxqfqt4iehoivclbj6snjpyof4za
    ONTO m17s2tswynm635anml2ci7ly2pa2nck2rcbvrhlznptqdoqa4t2pia
{
  ALTER TYPE default::Category {
      ALTER PROPERTY name {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  ALTER TYPE default::Category {
      ALTER PROPERTY name {
          DROP CONSTRAINT std::max_len_value(100);
      };
  };
};
