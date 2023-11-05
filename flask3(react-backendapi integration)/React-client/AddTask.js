import React, { useState } from 'react';
import axios from 'axios';

const AddTask = () => {
const [task, setTask] = useState('');

const handleAddTask = () => {
// Send a POST request to add a new task
axios.post('http://localhost:5000/tasks', { task })
.then(response => {
console.log('Task added:', response.data.message);
// Optionally, update the UI to reflect the new task
})
.catch(error => {
console.error('Error adding task:', error);
});

// Clear the input field
setTask('');
};

return (
<div>
<h2>Add Task</h2>
<input
type="text"
placeholder="Task"
value={task}
onChange={e => setTask(e.target.value)}
/>
<button onClick={handleAddTask}>Add Task</button>
</div>
);
};

export default AddTask;