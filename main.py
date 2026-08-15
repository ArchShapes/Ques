import os
import webview

# Get absolute path to index.html
html_path = os.path.abspath('index.html')

def main():
    # fullscreen=True starts the application over the entire display monitor
    window = webview.create_window(
        title='Dark Mode Window',
        url=f'file://{html_path}',
        fullscreen=True,
        background_color='#121212'
    )
    
    webview.start()

if __name__ == '__main__':
    main()
