import React from 'react';

function App() {
  return (
    <div style={{fontFamily:'Arial',padding:20}}>
      <h1>Daddy's Initiative Web Dashboard</h1>
      <p>Connect wallet · View NFTs · Toggle Autopilot</p>
      <button onClick={() => alert('Connect wallet (placeholder)')}>Connect Wallet</button>
      <div style={{marginTop:20}}>
        <h3>Net Worth</h3>
        <div>$12,480.32</div>
      </div>
    </div>
  );
}

export default App;
