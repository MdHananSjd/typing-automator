import pyautogui as pg
import time
from pynput import keyboard
import threading

# Use a global flag to indicate when the script should stop
stop_typing = False

def on_press(key):
    """Function to be called by the listener on a key press."""
    global stop_typing
    try:
        # Check if the pressed key is '§'
        if key.char == '§':
            print("\n§ key pressed. Stopping typing.")
            stop_typing = True
            return False  # Stop the listener
    except AttributeError:
        # Ignore special keys without a character, like Shift or Ctrl
        pass

def start_typing(text_to_write):
    """The main function to perform the typing."""
    global stop_typing
    for char in text_to_write:
        if stop_typing:
            print("Typing stopped by user.")
            break
        pg.write(char)
        # You can adjust the typing speed by adding a short delay
        # time.sleep(0.01)

    if not stop_typing:
        print("Typing complete.")

# The text you want to write
text_to_write = '''
import java.io.*;
import java.text.DecimalFormat;
public class Main {
public static void main(String[] args) throws Exception {
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
String logFile=br.readLine();
String reportFile=br.readLine();
int n=Integer.parseInt(br.readLine());
String[] logs=new String[n];
for(int i=0;i<n;i++){
logs[i]=br.readLine();
}
int errorCount=0;
for(String line:logs){
if(line.contains("ERROR")) errorCount++;
}
double errorPercentage=(errorCount*100.0)/n;
DecimalFormat df=new DecimalFormat("0.00");
System.out.println("=== Log File Contents ===");
for(String line:logs){
System.out.println(line);
}
System.out.println("=== Report File Contents ===");
System.out.println("Total log entries: "+n);
System.out.println("Error entries: "+errorCount);
System.out.println("Error percentage: "+df.format(errorPercentage)+"%");
BufferedOutputStream bos=new BufferedOutputStream(new FileOutputStream(reportFile));
PrintStream ps=new PrintStream(bos);
ps.println("Total log entries: "+n);
ps.println("Error entries: "+errorCount);
ps.println("Error percentage: "+df.format(errorPercentage)+"%");
ps.flush();
ps.close();
}
}

'''

# Start the keyboard listener in a separate thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Typing will start in 3 seconds...")
print("Press the '§' key at any time to stop.")
time.sleep(3)

# Start the typing process
start_typing(text_to_write)

# Wait for the listener thread to finish
listener.join()
