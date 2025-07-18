import customtkinter as ctk
import tkinter.messagebox as tkmb  # For pop-up messages

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"


class CricketScoreboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cricket Scoreboard")
        self.geometry("600x750")

        # --- Game State Variables ---
        self.runs = 0
        self.wickets = 0
        self.balls_bowled = 0  # Track balls to calculate overs accurately
        self.max_wickets = 10  # Standard for cricket
        self.overs_per_game = None  # Can be set for a full match limit if needed

        self._create_widgets()
        self._update_display()  # Initial display update

    def _create_widgets(self):
        # --- Score Display Frame ---
        score_display_frame = ctk.CTkFrame(
            self, fg_color="transparent"
        )  # Transparent for main window background
        score_display_frame.pack(pady=20, padx=20, fill="x")

        # Runs/Wickets Label (e.g., "123/4")
        self.label_score = ctk.CTkLabel(
            score_display_frame,
            text="0/0",
            font=("Arial", 70, "bold"),
            text_color="white",
        )
        self.label_score.pack(side="left", padx=(0, 20), expand=True)

        # Overs Label (e.g., "Overs: 12.3")
        self.label_overs = ctk.CTkLabel(
            score_display_frame,
            text="Overs: 0.0",
            font=("Arial", 40),
            text_color="white",
        )
        self.label_overs.pack(side="right", padx=(20, 0), expand=True)

        # --- Buttons Frame ---
        buttons_frame = ctk.CTkFrame(self, fg_color="black")
        buttons_frame.pack(pady=10, padx=20)

        # Run Buttons
        runs = [1, 2, 3, 4, 5, 6]
        row = 0
        col = 0
        for r in runs:
            button = ctk.CTkButton(
                buttons_frame,
                text=f"+{r}",
                font=("Arial", 30),
                command=lambda run=r: self._add_runs(run),
                width=100,
                height=70,
                corner_radius=10,
            )
            button.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 2:  # 3 buttons per row
                col = 0
                row += 1

        # Wicket Button
        self.button_wicket = ctk.CTkButton(
            buttons_frame,
            text="Wicket",
            font=("Arial", 30),
            command=self._add_wicket,
            width=200,
            height=70,
            fg_color="darkred",
            hover_color="red",
        )
        self.button_wicket.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

        # Extra/Wide/No Ball/Leg Bye (Optional, for more detailed scorekeeping)
        # You can uncomment and add logic for these if desired
        # self.button_extra = ctk.CTkButton(buttons_frame, text="Extra", font=("Arial", 30),
        #                                   command=self._add_extra,
        #                                   width=100, height=70)
        # self.button_extra.grid(row=row, column=2, padx=10, pady=10)

        # --- Control Buttons Frame ---
        control_frame = ctk.CTkFrame(self, fg_color="black")
        control_frame.pack(pady=20, padx=20, fill="x")

        # Reset Button
        self.button_reset = ctk.CTkButton(
            control_frame,
            text="Reset Score",
            font=("Arial", 25),
            command=self._reset_score,
            width=180,
            height=60,
            fg_color="gray",
            hover_color="darkgray",
        )
        self.button_reset.pack(side="left", expand=True, padx=10)

        # Undo Last Action (More complex, but good for real scoreboards)
        # self.button_undo = ctk.CTkButton(control_frame, text="Undo", font=("Arial", 25),
        #                                  command=self._undo_last_action,
        #                                  width=180, height=60, fg_color="orange", hover_color="darkorange")
        # self.button_undo.pack(side="right", expand=True, padx=10)

    def _update_display(self):
        """Updates the labels with current runs, wickets, and overs."""
        overs_full = self.balls_bowled // 6
        overs_balls = self.balls_bowled % 6
        self.label_score.configure(text=f"{self.runs}/{self.wickets}")
        self.label_overs.configure(text=f"Overs: {overs_full}.{overs_balls}")

    def _show_all_out_message(self):
        """Displays an alert when all batsmen are out."""
        tkmb.showinfo("All Out!", "All batsmen are out! Innings complete.")
        # Optionally disable all run/wicket buttons here
        self._toggle_buttons(False)

    def _toggle_buttons(self, enable: bool):
        """Enables or disables relevant buttons."""
        for (
            child
        ) in self.children.values():  # Iterate through all widgets in the window
            if isinstance(child, ctk.CTkFrame):
                for (
                    btn_child
                ) in child.winfo_children():  # Iterate through widgets in frames
                    if isinstance(btn_child, ctk.CTkButton) and btn_child not in [
                        self.button_reset
                    ]:  # Exclude reset
                        btn_child.configure(state="normal" if enable else "disabled")
        # Specifically re-enable reset button
        self.button_reset.configure(state="normal")

    def _add_runs(self, run_value):
        """Adds runs to the score and updates overs."""
        if self.wickets < self.max_wickets:
            self.runs += run_value
            self.balls_bowled += 1
            self._update_display()
            if (
                self.wickets == self.max_wickets
            ):  # Check again after adding runs if a wicket might have caused "all out" from previous action
                self._show_all_out_message()
        else:
            self._show_all_out_message()

    def _add_wicket(self):
        """Adds a wicket to the score."""
        if self.wickets < self.max_wickets:
            self.wickets += 1
            self.balls_bowled += 1  # A wicket also counts as a ball
            self._update_display()
            if self.wickets == self.max_wickets:
                self._show_all_out_message()
        else:
            self._show_all_out_message()

    def _reset_score(self):
        """Resets all score variables to zero."""
        confirm = tkmb.askyesno(
            "Reset Score", "Are you sure you want to reset the score?"
        )
        if confirm:
            self.runs = 0
            self.wickets = 0
            self.balls_bowled = 0
            self._update_display()
            self._toggle_buttons(True)  # Re-enable buttons after reset


# --- Main execution ---
if __name__ == "__main__":
    app = CricketScoreboard()
    app.mainloop()
