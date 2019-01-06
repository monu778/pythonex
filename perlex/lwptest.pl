 use LWP::UserAgent;
  my $ua = LWP::UserAgent->new;
  $ua->agent("MyApp/0.1 ");

  # Create a request
  my $req = HTTP::Request->new(GET => 'https://jira.broadsoft.com/secure/attachment/867286/localhost_access_log.2018-05-19.txt');
  #$req->content_type('application/x-www-form-urlencoded');
  $req->content();

  # Pass request to the user ag////ent and get a response back
  my $res = $ua->request($req);

  # Check the outcome of the response
  if ($res->is_success) {
      print $res->content;
  }
  else {
      print $res->status_line, "\n";
  }
