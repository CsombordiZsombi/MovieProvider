CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass VARCHAR(70) NOT NULL,
    rank VARCHAR(50) NOT NULL DEFAULT 'basic'
        CHECK (rank IN ('basic', 'premium', 'admin'))
);

INSERT INTO users (username, pass, rank) VALUES ('admin', '$2b$12$zE1XJu95RzsZIoqOFyhVReTnvO0x4hjyzIWd26v3gRNr5Ps9XVKxe', 'admin');
INSERT INTO users (username, pass) VALUES ('test', '$2b$12$3Rg979U0IfkfK8OaABblF.Kr1XoggEajk2V/UgWiMXQHI.R0AcRCy');
INSERT INTO users (username, pass) VALUES ('basic', '$2b$12$inbyP06odHbDCH5PORvzOewHJ9SuqBd7FbzHii62e1PE90F06fNOC');
INSERT INTO users (username, pass, rank) VALUES ('premium', '$2b$12$Ft4R6U7RScEMLOxO6lB2Lujg82vfYrSaZXZ5GKbis45Y3AidQ7aSm', 'premium');

CREATE TABLE games(
    game_id SERIAL PRIMARY KEY,
    game_name VARCHAR(50) UNIQUE NOT NULL,
    game_owner VARCHAR(50),

    CONSTRAINT fk_game_owner 
        FOREIGN KEY (game_owner) 
        REFERENCES users(username)
        ON DELETE CASCADE 
);