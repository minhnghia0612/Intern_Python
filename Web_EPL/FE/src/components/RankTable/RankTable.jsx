import React from "react";
import "./RankTable.css";

function RankTable({ ranks }) {
  return (
    <div className="rank-container">
      <h2 className="rank-title">Bảng xếp hạng</h2>
      <table className="rank-table">
        <thead>
          <tr>
            <th>Pos</th>
            <th className="right-align">Team</th>
            <th>MP</th>
            <th>W</th>
            <th>D</th>
            <th>L</th>
            <th>GD</th>
            <th>Pts</th>
          </tr>
        </thead>
        <tbody>
          {ranks.map((item) => (
            <tr key={item.id}>
              <td>{item.rank}</td>
              <td className="team-cell">
                  <img src={item.team.logo} alt={item.team.name} className="team-logo" />
                  <span>{item.team.name}</span>
              </td>
              <td>{item.matched_played}</td>
              <td>{item.win}</td>
              <td>{item.draw}</td>
              <td>{item.lose}</td>
              <td>{item.gd}</td>
              <td className="bold">{item.points}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default RankTable;
