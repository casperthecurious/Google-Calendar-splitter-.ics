def split_ics_file(input_file, max_size_kb=400, output_prefix='calendar_part_'):
    import os

    # Convert KB to bytes for comparison
    max_size = max_size_kb * 1024

    # Read the original file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the calendar's header and footer
    header = content[:content.find('BEGIN:VEVENT')]
    footer = 'END:VCALENDAR'
    
    # Split into individual events
    events = content.split('BEGIN:VEVENT')[1:]
    events = ['BEGIN:VEVENT' + event for event in events]
    
    # Initialize variables for splitting
    current_chunk = []
    current_size = len(header.encode('utf-8')) + len(footer.encode('utf-8'))
    chunk_number = 1

    # Create output folder in same directory as input file
    base_dir = os.path.dirname(os.path.abspath(input_file))
    output_dir = os.path.join(base_dir, "calendar_parts")
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each event
    for event in events:
        event_size = len(event.encode('utf-8'))
        
        if current_size + event_size > max_size:
            output_file = os.path.join(output_dir, f'{output_prefix}{chunk_number}.ics')
            write_chunk(header, current_chunk, footer, output_file)

            # Start new chunk
            current_chunk = [event]
            current_size = len(header.encode('utf-8')) + len(footer.encode('utf-8')) + event_size
            chunk_number += 1
        else:
            current_chunk.append(event)
            current_size += event_size
    
    # Write the last chunk if it contains any events
    if current_chunk:
        output_file = os.path.join(output_dir, f'{output_prefix}{chunk_number}.ics')
        write_chunk(header, current_chunk, footer, output_file)

def write_chunk(header, events, footer, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(header)
        for event in events:
            f.write(event)
        f.write(footer)
    print(f"Wrote {output_file} with {len(events)} events")


# Usage example
split_ics_file('calendar-to-split.ics', max_size_kb=400)  # Split into ~400KB chunks
