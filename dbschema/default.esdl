module default {

type Book {
    required property title -> str {
        constraint max_len_value(200)
    }
    property author -> str {
        constraint max_len_value(200)
    }
    required link category -> Category
}

type Category {
    required property name -> str {
        constraint max_len_value(100)
    }
}

type User {
    required property username -> str {
        constraint max_len_value(100)
    }
    property full_name -> str {
        constraint max_len_value(200)
    }
    multi link borrowed_books -> Book {
    }
}

}