CREATE TABLE to_do (
    action_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    action_name TEXT NOT NULL,
    action_type TEXT NOT NULL,
    allocated_time INTEGER NOT NULL,
    action_due_date DATE NOT NULL,
    action_completed BOOLEAN NOT NULL DEFAULT FALSE
);