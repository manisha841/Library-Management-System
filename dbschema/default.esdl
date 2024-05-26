module default {

type Book {
    required title: str {
        constraint max_len_value(200);
    }
    author: str {
        constraint max_len_value(200);
    }
    required category: Category;
    borrower: User;
    is_borrowed: bool;
};

type Category {
    required name: str {
        constraint exclusive;
    }
};

type User {
    full_name: str {
        constraint max_len_value(200);
    }
};

}
