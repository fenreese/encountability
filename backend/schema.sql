CREATE TYPE request_status AS ENUM ('pending', 'accepted', 'declined');

CREATE TABLE IF NOT EXISTS clients (
    email_address VARCHAR NOT NULL,
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS friendships (
    client_id VARCHAR REFERENCES clients (id),
    friend_id VARCHAR REFERENCES clients (id),
    CHECK (client_id < friend_id),
    PRIMARY KEY (client_id, friend_id)
);

CREATE TABLE IF NOT EXISTS money_requests (
    id VARCHAR PRIMARY KEY,
    requester_id VARCHAR REFERENCES clients (id),
    requestee_id VARCHAR REFERENCES clients (id),
    amount INT NOT NULL,
    paid_amount INT NOT NULL DEFAULT 0,
    message VARCHAR,
    status request_status
);

CREATE TABLE IF NOT EXISTS group_requests (
    id VARCHAR PRIMARY KEY,
    requester_id VARCHAR REFERENCES clients (id),
    amount INT NOT NULL,
    paid_amount INT NOT NULL DEFAULT 0,
    message VARCHAR
);

CREATE TABLE IF NOT EXISTS group_requests_list (
    id VARCHAR PRIMARY KEY REFERENCES money_requests (id),
    group_request_id VARCHAR REFERENCES group_requests (id),
    requester_id VARCHAR REFERENCES clients (id),
    amount INT NOT NULL,
    paid_amount INT NOT NULL DEFAULT 0,
    message VARCHAR
);