import React from 'react';
import './App.css';
import MyComponent from './displaytable';


class App extends React.Component {
  render () {
    return(
      <div className='App'>
        <MyComponent />        
      </div>
    );
  }
}

export default App ;
