INSERT INTO clients (email_address, id, name) VALUES 
('reese@renys.dev', '6113df03-1718-46d0-8ef4-fdb14f78cf43', 'Reese'),
('goose@emily.engineer', '57124ec0-eaa9-4b11-b85a-739d1c5bff5d', 'Psyduck'),
('pik@chu.com', '5a6c6169-5ebd-41d5-ac4e-d257dde56017', 'Pikachu'),
('h@xor.us', 'fe53445f-e766-4e46-a5b4-7de132d6181d', 'Haxorus');

INSERT INTO friendships (client_id, friend_id) VALUES
('57124ec0-eaa9-4b11-b85a-739d1c5bff5d', '5a6c6169-5ebd-41d5-ac4e-d257dde56017'),
('5a6c6169-5ebd-41d5-ac4e-d257dde56017', 'fe53445f-e766-4e46-a5b4-7de132d6181d'),
('5a6c6169-5ebd-41d5-ac4e-d257dde56017', '6113df03-1718-46d0-8ef4-fdb14f78cf43');
