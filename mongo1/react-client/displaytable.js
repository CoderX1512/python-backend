import React, { useEffect, useState } from 'react';
import axios from 'axios';

function MyComponent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const apiUrl = 'http://127.0.0.1:5000/employees';

    axios.get(apiUrl)
      .then((response) => {
        
        setData(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Data Table</h1>
      <table border={1}>
        <thead>
          <tr>
            <th>ID</th> 
            <th>Name</th>
            <th>Age</th>
            <th>Position</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr>
              <td key={item._id}>{item._id}</td>
              <td>{item.name}</td>
              <td>{item.age}</td>
              <td>{item.position}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default MyComponent;