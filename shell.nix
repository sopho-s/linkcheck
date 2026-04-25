{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    buildInputs = with pkgs; [
        docker
        python3
        mitmproxy
        python312Packages.mitmproxy
        python312Packages.cryptography
        python312Packages.paramiko
        python312Packages.requests
    ];
}