import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Tasks = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        // Fetch tasks from the Flask API
        axios.get('http://localhost:5000/tasks')
            .then(response => {
                setTasks(response.data);
            })
            .catch(error => {
                console.error('Error fetching tasks:', error);
            });
    }, []);

    return (
        <div>
            <h1>Tasks</h1>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>{task.task}</li>
                ))}
            </ul>
        </div>
    );
};

export default Tasks;