import customtkinter
from pytube import YouTube, Playlist, exceptions


class App(customtkinter.CTk):
    def download_vids(self):
        links = self.link_input.get()
        link_list = links.split(",")
        self.total_vids = len(link_list)
        self.videos_downloaded = 0
        self.amount_done.configure(text=f"{self.videos_downloaded}/{self.total_vids}")
        for vid in link_list:
            self.progress_bar.set(0)
            try:
                yt = YouTube(vid, on_progress_callback=self.progress_update)
                self.amount_done.configure(
                    text=f"{yt.title}   {self.videos_downloaded}/{self.total_vids}"
                )
                yt.streams.get_highest_resolution().download(self.download_location_var)
                self.videos_downloaded += 1
            except exceptions.AgeRestrictedError:
                self.status.configure(text=f"{yt.title} is AGE RESTRICTED")
        self.status.configure(text="Done")
        app.title("Youtube Video Downloader")
        self.download_location.configure(text="Location")

    def __init__(self):
        super().__init__()
        self.geometry("750x400")
        self.title("Youtube Video Downloader")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=0)

        self.vid_or_playlist_combobox = customtkinter.CTkComboBox(
            self,
            values=["Video", "Playlist"],
            justify="center",
        )
        self.vid_or_playlist_combobox.pack(pady=10)

        self.download_location_var = None
        self.download_location = customtkinter.CTkButton(
            self, text="Location", command=self.select_location
        )
        self.download_location.pack()

        self.vid_or_playlist_combobox.pack()
        self.link_label = customtkinter.CTkLabel(
            self, text="Youtube link (separate multiple links with a comma)"
        )
        self.link_label.pack()

        self.link_input = customtkinter.CTkEntry(self, width=350, height=45)
        self.link_input.pack()

        self.progrees_per = customtkinter.CTkLabel(self, text="")
        self.progrees_per.pack(pady=(10, 5))

        self.progress_bar = customtkinter.CTkProgressBar(self, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(10, 0))

        self.links = customtkinter.StringVar()
        self.download_button = customtkinter.CTkButton(
            self, text="Download", command=self.download_choice, fg_color="red"
        )
        self.download_button.pack(pady=(20, 0))

        self.amount_done = customtkinter.CTkLabel(self, text="")
        self.amount_done.pack(pady=(20, 0))

        self.status = customtkinter.CTkLabel(self, text="")
        self.status.pack(pady=(20, 0))

    def select_location(self):
        self.download_location_var = customtkinter.filedialog.askdirectory()
        self.download_location.configure(text=self.download_location_var)

    def progress_update(self, stream, chunk, bytes_remaining):
        total = stream.filesize
        bytes_downloaded = total - bytes_remaining
        percent_done = bytes_downloaded / total
        per = int(percent_done * 100)
        self.progrees_per.configure(text=f"{per}%")
        self.progrees_per.update()
        self.progress_bar.set(percent_done)

    def download_choice(self):
        self.combo_var = self.vid_or_playlist_combobox.get()
        if self.combo_var == "Video":
            self.download_vids()


if __name__ == "__main__":
    app = App()
    app.mainloop()
