CREATE TABLE article (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    ingredients JSONB,
    steps JSONB,
    has_image BOOLEAN,
    has_tags BOOLEAN,
    category VARCHAR(50),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    nickname VARCHAR(50) NOT NULL,
    credential VARCHAR(100) NOT NULL
);

CREATE TABLE role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

CREATE TABLE user_role (
    user_id INT,
    role_id INT,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (role_id) REFERENCES role(id)
);



CREATE TABLE user_article (
    user_id INT,
    article_id INT,
    PRIMARY KEY (user_id, article_id),
    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (article_id) REFERENCES article(id)
);

CREATE TABLE tag (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

CREATE TABLE article_tag (
    article_id INT,
    tag_id INT,
    PRIMARY KEY (article_id, tag_id),
    FOREIGN KEY (article_id) REFERENCES article(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id)
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    user_id INT,
    article_id INT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (article_id) REFERENCES article(id)
);

CREATE TABLE image (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255),
    alt_text VARCHAR(255),
    article_step INT
);

CREATE TABLE article_image (
    article_id INT,
    image_id INT,
    PRIMARY KEY (article_id, image_id),
    FOREIGN KEY (article_id) REFERENCES article(id),
    FOREIGN KEY (image_id) REFERENCES image(id)
);
