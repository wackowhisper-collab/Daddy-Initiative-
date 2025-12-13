Extras included in this ZIP:
- ios/WalletConnectExample.swift : example placeholder for WalletConnect integration
- backtest/backtest.py : sample backtest harness (generate prices + SMA strategy)
- web/ : React dashboard skeleton (src/App.js, src/index.js)
- nft_metadata/ : 5 sample NFT metadata JSON files (replace IPFS hashes)
- design_mockups/ : PNG mockups for Home, Investing, Queen B screens

How to use:
- iOS: copy WalletConnectExample.swift into Xcode project; follow WalletConnect SDK docs to complete integration.
- Backtest: python3 backtest/backtest.py (requires pandas, numpy)
- Web: cd web && npm install && npm start (install react-scripts if needed)
- NFT: update image IPFS links and pin via Pinata/IPFS provider.
