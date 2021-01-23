import React, {Component} from 'react'
import TopMovies from './components/TopMovies'
import Navbar from './components/Navbar'

export default class App extends Component {
  render() {
    return <>
      <Navbar />
      <TopMovies />
    </>
  }

}
  