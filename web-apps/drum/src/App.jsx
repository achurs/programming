import './App.css'

function App() {

  return (
    <>
      <div className='container' id='drum-machine'>
        <div id='display'></div>
        <div className="row">
          <div className="col"><button className='drum-pad' id='Q'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Heater-1.mp3" className='clip' id='Q'></audio>Q</button></div>
          <div className="col"><button className='drum-pad' id='W'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Heater-2.mp3" className='clip' id='W'></audio>W</button></div>
          <div className="col"><button className='drum-pad' id='E'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Heater-3.mp3" className='clip' id='E'></audio>E</button></div>
        </div>
        <div className="row">
          <div className="col"><button className='drum-pad' id='A'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Heater-4_1.mp3" className='clip' id='A'></audio>A</button></div>
          <div className="col"><button className='drum-pad' id='S'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Heater-6.mp3" className='clip' id='S'></audio>S</button></div>
          <div className="col"><button className='drum-pad' id='D'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Dsc_Oh.mp3" className='clip' id='D'></audio>D</button></div>
        </div>
        <div className="row">
          <div className="col"><button className='drum-pad' id='Z'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Kick_n_Hat.mp3" className='clip' id='Z'></audio>Z</button></div>
          <div className="col"><button className='drum-pad' id='X'><audio src="https://s3.amazonaws.com/freecodecamp/drums/RP4_KICK_1.mp3" className='clip' id='X'></audio>X</button></div>
          <div className="col"><button className='drum-pad' id='C'><audio src="https://s3.amazonaws.com/freecodecamp/drums/Cev_H2.mp3" className='clip' id='C'></audio>C</button></div>
        </div>
      </div>
    </>
  )
}

export default App
