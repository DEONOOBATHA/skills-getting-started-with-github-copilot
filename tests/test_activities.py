def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_expected_activity_data(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()

    assert isinstance(payload, dict)
    assert expected_activity in payload
    assert payload[expected_activity]["description"] == "Learn strategies and compete in chess tournaments"
    assert payload[expected_activity]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert payload[expected_activity]["max_participants"] == 12
    assert payload[expected_activity]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]