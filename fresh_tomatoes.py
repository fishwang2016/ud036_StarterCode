import webbrowser
import os
import re
import media

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
   
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    
     <link rel="stylesheet" href="css/styles.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
   
 
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

# the following are the movie instances
    
showgirls = media.Movie(
    "https://youtu.be/gszDLDFwcLk",
    "Show Girls",
    "https://thenypost.files.wordpress.com/2016/06/bechdel.jpg?quality=90&strip=all&w=664&h=441&crop=1") #noqa

approach_unknow=media.Movie(
  "https://youtu.be/CQx2eosUlXY",
  "Approaching the Unknown",
  "https://thenypost.files.wordpress.com/2016/06/m45.jpg?quality=90&strip=all&w=664&h=441&crop=1") #noqa

time_to_choose=media.Movie(
  "https://youtu.be/Xj6-oIyXM20",
  "Time to Choose",
  "https://thenypost.files.wordpress.com/2016/06/chinese_masks.jpg?quality=90&strip=all&w=664&h=441&crop=1")#noqa

the_witness =media.Movie(
  "https://youtu.be/gpU6UVfIQLM",
  "The Witness",
  "https://thenypost.files.wordpress.com/2016/06/kitty_genovese.jpg?quality=90&strip=all&w=664&h=441&crop=1")#noqa

popstar = media.Movie(
  "https://youtu.be/S207jSgL_jw",
  "Popstar",
  "https://thenypost.files.wordpress.com/2016/06/popstar-_never_stop_never_stopping_-2016.jpg?quality=90&strip=all&w=664&h=441&crop=1")#noqa

me_before_you = media.Movie(
  "https://youtu.be/Eh993__rOxA",
  "Me Before You",
  "https://thenypost.files.wordpress.com/2016/06/me_before_you.jpg?quality=90&strip=all&w=664&h=441&crop=1")#noqa

monthly_report= media.Movie(
  "https://youtu.be/cbw9hlBnG74",
  "Minority Report",
  "https://thenypost.files.wordpress.com/2016/05/adaptations.jpg?quality=90&strip=all&w=664&h=441&crop=1")#noqa

alice_eyes = media.Movie(
  "https://youtu.be/x3IWwnNe5mc",
  "Alice Through the Looking Glass",
  "https://thenypost.files.wordpress.com/2016/06/gettyimages-533878914.jpg?quality=90&strip=all&w=664&h=441&crop=1")#noqa

top_gun =media.Movie(
  "https://youtu.be/ioWpe3hdFH0",
  "Top Gun",
  "https://thenypost.files.wordpress.com/2016/05/topgun2a.jpg?quality=90&strip=all&strip=all")#noqa

# put movie instances into a list
movies =[showgirls,approach_unknow,time_to_choose,the_witness,popstar,me_before_you,monthly_report,alice_eyes,top_gun]

# calling open_movies_page() function to generate a html page.
open_movies_page(movies)