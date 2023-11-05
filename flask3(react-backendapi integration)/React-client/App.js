import React from 'react';
import './App.css';
import Tasks from  './components/Tasks';
import AddTask from  './components/AddTask';

class App extends React.Component {
  render () {
    return(
      <div className='App'>
        <Tasks />
        <AddTask />
      </div>
    );
  }
}

export default App ;
