#!/usr/bin/env python3
"""
Marriott Multi-Cloud Network Sync Platform - Web Server
Serves the presentation hub and all related resources
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket
import threading

class NetworkSyncHTTPHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler that redirects root to presentation hub"""
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/presentation_hub.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

def find_free_port(start_port=8080):
    """Find an available port starting from start_port"""
    port = start_port
    while port < 65535:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            port += 1
    raise RuntimeError("No free ports available")

def open_browser(url):
    """Open browser after a short delay to ensure server is ready"""
    threading.Timer(1.5, lambda: webbrowser.open(url)).start()

def main():
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Find available port
    port = find_free_port(8080)
    server_address = ('', port)
    
    # Create server
    httpd = HTTPServer(server_address, NetworkSyncHTTPHandler)
    
    # Print startup message
    print("\n" + "="*60)
    print("🌐 Marriott Multi-Cloud Network Sync Platform")
    print("="*60)
    print(f"\n✅ Server started on http://localhost:{port}")
    print("\n📊 Opening presentation hub in your browser...")
    print("\n💡 Available resources:")
    print(f"   - Presentation Hub: http://localhost:{port}/")
    print(f"   - Main Presentation: http://localhost:{port}/cloud_agnostic_presentation.html")
    print(f"   - Architecture: http://localhost:{port}/architecture_visualization.html")
    print(f"   - Interactive Demo: http://localhost:{port}/interactive_demo.html")
    print(f"   - Working Demo: http://localhost:{port}/working_demo.html")
    print("\n⌨️  Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    # Open browser
    open_browser(f"http://localhost:{port}")
    
    # Start server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped")
        httpd.shutdown()
        sys.exit(0)

if __name__ == '__main__':
    main()