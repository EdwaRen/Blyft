import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './submit.js'

class App extends Component {
  render() {
    return (
      <div className="App">
      <banner>
      <img src="banner.jpg" alt="banner" width ="500" height="240"/>
      </banner>
        <header >
          <img src={logo} className="App-logo" alt="logo" />
          

        </header>
          <Login/>
      </div>
    );
  }
}

export default App;
