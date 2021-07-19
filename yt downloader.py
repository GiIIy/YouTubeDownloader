from pytube import YouTube 
import tkinter as tk


class YoutubeDownload:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(350, 100) )
        self.window.configure(bg="#000000")
        self.window.title("Youtube downloader")
        
        self.l_label = tk.Label(self.window, text = "Download Link")
        self.l_label.grid(column = 0, row = 0)
        
        self.n_label = tk.Label(self.window, text = "Save File as")
        self.n_label.grid(column = 0, row = 1)
        
        self.p_label = tk.Label(self.window, text = "Save File Path")
        self.p_label.grid(column = 0, row = 2)


        
        
        
        self.l_entry = tk.Entry(master = self.window, width = 40)
        self.l_entry.grid(column = 1, row = 0)
        
        self.n_entry = tk.Entry(master= self.window, width = 40)
        self.n_entry.grid(column = 1, row = 1)
        
        self.p_entry = tk.Entry(master = self.window, width = 40 )
        self.p_entry.grid(column = 1, row = 2)
        
        self.download_button = tk.Button(self.window, text = "Download", command = self.get_link)
        self.download_button.grid(column = 1, row = 4)

        return


    def download(self, link, save_path = "", save_name = ""):
        
        yt = YouTube(link) 
        yt_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        yt_stream.download(output_path = save_path, filename = save_name)

        return

  
    def get_link(self):
        link = self.l_entry.get()
        path = self.p_entry.get()
        name = self.n_entry.get()

        self.download(link, path, name)
        
        return

    def run(self):
        self.window.mainloop()
        return
    

if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run()
    
