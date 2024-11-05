sudo apt update
sudo apt install -y libglib2.0-0 libpango-1.0-0 libfontconfig1 libpangoft2-1.0-0

python3 -m venv myenv
source myenv/bin/activate

pip install streamlit WeasyPrint

echo "Installation completed. You can activate your environment using 'source myenv/bin/activate'."
