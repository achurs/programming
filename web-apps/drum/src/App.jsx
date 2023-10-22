import './App.css'

function App() {

  return (
    <>
      <div className='container' id='drum-machine'>
        <div className="row">
          <div className="col"><button onClick={() => console.log('clicked 1')}>1</button></div>
          <div className="col"><button>click</button></div>
          <div className="col"><button>click</button></div>
        </div>
        <div className="row">
          <div className="col"><button>click</button></div>
          <div className="col"><button>click</button></div>
          <div className="col"><button>click</button></div>
        </div>
        <div className="row">
          <div className="col"><button>click</button></div>
          <div className="col"><button>click</button></div>
          <div className="col"><button>click</button></div>
        </div>
      </div>
    </>
  )
}

export default App
