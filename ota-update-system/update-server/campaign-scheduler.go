package updateserver

type CampaignWave struct {
	Index        int
	VehicleIDs   []string
	TargetRatio  float64
	CanPromoteAB bool
}

type Campaign struct {
	TargetVersion string
	Waves         []CampaignWave
}

type CampaignScheduler struct {
	tracker *FleetTracker
}

func NewCampaignScheduler(tracker *FleetTracker) *CampaignScheduler {
	return &CampaignScheduler{tracker: tracker}
}

func (scheduler *CampaignScheduler) BuildCampaign(targetVersion string, firstWavePercent int) Campaign {
	snapshot := scheduler.tracker.Snapshot()
	vehicleIDs := make([]string, 0, len(snapshot))
	for _, record := range snapshot {
		vehicleIDs = append(vehicleIDs, record.VehicleID)
	}

	if firstWavePercent <= 0 {
		firstWavePercent = 10
	}
	if firstWavePercent > 100 {
		firstWavePercent = 100
	}

	firstWaveSize := (len(vehicleIDs) * firstWavePercent) / 100
	if firstWaveSize == 0 && len(vehicleIDs) > 0 {
		firstWaveSize = 1
	}

	firstWave := CampaignWave{
		Index:        1,
		VehicleIDs:   append([]string(nil), vehicleIDs[:firstWaveSize]...),
		TargetRatio:  float64(firstWavePercent) / 100.0,
		CanPromoteAB: scheduler.tracker.HealthyFraction() >= 0.8,
	}

	remaining := CampaignWave{
		Index:        2,
		VehicleIDs:   append([]string(nil), vehicleIDs[firstWaveSize:]...),
		TargetRatio:  1.0,
		CanPromoteAB: scheduler.tracker.HealthyFraction() >= 0.9,
	}

	waves := []CampaignWave{firstWave}
	if len(remaining.VehicleIDs) > 0 {
		waves = append(waves, remaining)
	}

	return Campaign{TargetVersion: targetVersion, Waves: waves}
}
