#!/bin/bash
# CodeLab Thailand — Local preview server
# Double-click (Mac) to preview slides locally.
cd "$(dirname "$0")"
PORT=8000
echo "═══════════════════════════════════════════════════════"
echo "  🚀 CodeLab Thailand — Slide Preview Server"
echo "  http://localhost:$PORT"
echo ""
echo "  Foundation 1:  http://localhost:$PORT/f1/ss1/index.html"
echo "  Foundation 2:  http://localhost:$PORT/f2/ss6/index.html"
echo "  Ctrl+C เพื่อหยุด server"
echo "═══════════════════════════════════════════════════════"
if [[ "$OSTYPE" == "darwin"* ]]; then
    sleep 1 && open "http://localhost:$PORT/f1/ss1/index.html" &
fi
python3 -m http.server $PORT
