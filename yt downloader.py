from pytube import YouTube 
from playsound import playsound
import tkinter as tk


class YoutubeDownloader:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(350, 100) )
        self.window.configure(bg="#000000")
        self.window.title("Youtube downloader")
        
        self.link_label = tk.Label(self.window, text = "Download Link")
        self.link_label.grid(column = 0, row = 0)
        
        self.name_label = tk.Label(self.window, text = "Save File as")
        self.name_label.grid(column = 0, row = 1)
        
        self.path_label = tk.Label(self.window, text = "Save File Path")
        self.path_label.grid(column = 0, row = 2)


        
        
        
        self.link_entry = tk.Entry(master = self.window, width = 40)
        self.link_entry.grid(column = 1, row = 0)
        
        self.name_entry = tk.Entry(master= self.window, width = 40)
        self.name_entry.grid(column = 1, row = 1)
        
        self.path_entry = tk.Entry(master = self.window, width = 40 )
        self.path_entry.grid(column = 1, row = 2)
        
        self.download_button = tk.Button(self.window, text = "Download", command = self.get_link)
        self.download_button.grid(column = 1, row = 4)

        return


    def download(self, link, save_path = "", save_name = ""):
        
        yt = YouTube(link) 
        yt_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        yt_stream.download(output_path = save_path, filename = save_name)

        return

  
    def get_link(self):
        link = self.link_entry.get()
        path = self.path_entry.get()
        name = self.name_entry.get()

        self.download(link, path, name)
        
        return

    def run(self):
        self.window.mainloop()
        return
    

if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run()
    
