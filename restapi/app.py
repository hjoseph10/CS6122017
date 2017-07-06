#!/usr/bin/python
from flask import Flask, jsonify, url_for, make_response, abort

app = Flask(__name__)

nbateams = [
    {
        'id': 1,
        'Name': u'San Antonio Spurs',
        'Location': u'San Antonio, TX',
        'Head Coach': u'Gregg Popovich',
        'Star Player': u'Kawhi Leonard',
    },
    {
        'id': 2,
        'Name': u'New York Knicks',
        'Location': u'New York, NY',
        'Head Coach': u'Jeff Hornacek',
        'Star Player': u'Carmelo Anthony',
    },
    {
        'id': 3,
        'Name': u'Brooklyn Nets',
        'Location': u'Brooklyn, NY',
        'Head Coach': u'Kenny Atkinson',
        'Star Player': u'Jeremy Lin',
    },
    {
        'id': 4,
        'Name': u'Boston Celtics',
        'Location': u'Boston, MA',
        'Head Coach': u'Brad Stevens',
        'Star Player': u'Isaiah Thomas',
    },
    {
        'id': 5,
        'Name': u'Los Angeles Lakers',
        'Location': u'Los Angeles, LA',
        'Head Coach': u'Luke Walton',
        'Star Player': u'Lonzo Ball',
    },
]


def make_public(team):
    new_team = {}
    for field in team:
        if field == 'id':
            new_team['uri'] = url_for('get_team', team_id=team['id'], _external=True)
        else:
            new_team[field] = team[field]
    return new_team


@app.route('/api/v1.0/teams', methods=['GET'])
def get_teams():
    return jsonify({'nbateams': [make_public(team) for team in nbateams]})


@app.route('/api/v1.0/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = [team for team in nbateams if team['id'] == team_id]
    if len(team) == 0:
        abort(404)
    return jsonify({'team': team[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Your team was not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
