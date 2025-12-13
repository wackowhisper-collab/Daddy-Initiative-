// WalletConnectExample.swift
// Uses WalletConnect v2 concepts - placeholder integration notes included.
import Foundation
import SwiftUI
// NOTE: Install WalletConnect SDK for iOS per docs. This file shows a pattern for connecting and requesting a signature.

struct WalletConnectExampleView: View {
    @State private var connectedAddress: String? = nil
    var body: some View {
        VStack(spacing:20) {
            Text("WalletConnect Example").font(.headline)
            if let addr = connectedAddress {
                Text("Connected: \(addr)")
            } else {
                Button("Connect Wallet") {
                    connectWallet()
                }
            }
            Button("Request Signature") { requestSignature() }
        }.padding()
    }

    func connectWallet() {
        // PSEUDOCODE:
        // let client = WalletConnectClient()
        // let session = try await client.connect(...)
        // connectedAddress = session.accounts.first
        connectedAddress = "0xDEMO_WALLETCONNECT_ADDRESS"
        print("Wallet connected (placeholder)")
    }

    func requestSignature() {
        guard connectedAddress != nil else { return }
        // PSEUDOCODE: request personal_sign or EIP-712 via WalletConnect client
        print("Requesting signature (placeholder)")
    }
}
